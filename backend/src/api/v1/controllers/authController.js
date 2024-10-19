import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';
import { AdminModel } from '../models/adminSchema.js';
import { UserModel } from '../models/userSchema.js';

const JWT_SECRET = process.env.JWT_SECRET_KEY || 'LMAaWJ9zZDHdeLFh0f9072K7lui4QynjrIZZ4Uigiow';
const JWT_EXPIRES_IN = process.env.JWT_EXPIRES_IN || '1h';

// Function to find a user by email based on role
export const findUserByEmail = async (email, role) => {
    if (role === 'Admin') {
        return await AdminModel.findOne({ email });
    } else if (role === 'User') {
        return await UserModel.findOne({ email });
    }
    return null;
};

export const registerUserGeneral = async (req, res) => {
    const { fullName, lastName, email, password } = req.body; 
    try { 
        // Check if the email is already registered
        const existingUser = await UserModel.findOne({ email });
        if (existingUser) {
            return res.status(400).json({ message: 'Email already registered' });
        }

        // Hash the password before saving
        const hashedPassword = await bcrypt.hash(password, 10);

        // Create the new user and associate with the logged-in admin
        const newUser = new UserModel({ 
            fullName, 
            lastName, 
            email, 
            password: hashedPassword,
            createdBy: req.user._id // Use the ID of the logged-in admin directly
        });

        await newUser.save();
        res.status(201).json({ message: 'User registered successfully' });
    } catch (error) {
        res.status(500).json({ message: 'Server error', error });
    }
};
// Admin registration function
export const registerAdmin = async (req, res) => {
    const { firstName, lastName, email, password, companyName, field } = req.body; 
    try {
        const existingAdmin = await AdminModel.findOne({ email });
        if (existingAdmin) {
            return res.status(400).json({ message: 'Email already registered' });
        }

        const hashedPassword = await bcrypt.hash(password, 10);       
        const newAdmin = new AdminModel({ 
            firstName, 
            lastName, 
            email, 
            password: hashedPassword,
            companyName, 
            field 
        });

        await newAdmin.save();
        res.status(201).json({ message: 'Admin registered successfully' });
    } catch (error) {
        res.status(500).json({ message: 'Server error', error });
    }
};

export const loginUser = async (req, res) => {
    const { email, password, role } = req.body; // Add 'role' in request to differentiate users
    try {
        // Find user based on the role (Admin or User)
        const user = await findUserByEmail(email, role);

        if (!user) {
            return res.status(404).json({ message: `${role} not found` });
        }

        // Compare the password
        const isMatch = await bcrypt.compare(password, user.password);
        if (!isMatch) {
            return res.status(400).json({ message: 'Invalid credentials' });
        }

        // Generate JWT token
        const token = jwt.sign({ id: user._id, role }, JWT_SECRET, {
            expiresIn: JWT_EXPIRES_IN,
        });

        res.status(200).json({ token, role });
    } catch (error) {
        res.status(500).json({ message: 'Server error', error });
    }
};