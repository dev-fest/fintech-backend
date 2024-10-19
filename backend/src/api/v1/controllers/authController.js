import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';
import User from '../models/userSchema.js';
const JWT_SECRET = process.env.JWT_SECRET_KEY || 'LMAaWJ9zZDHdeLFh0f9072K7lui4QynjrIZZ4Uigiow';
const JWT_EXPIRES_IN = process.env.JWT_EXPIRES_IN || '24h';
export const findUserByEmail = async (email) => {
    return await User.findOne({ email });
};
export const registerUserGeneral = async (req, res) => {
    const { firstName, lastName, email, password, role_id } = req.body;  
    try {   
        const existingUser = await User.findOne({ email });
        if (existingUser) {
            return res.status(400).json({ message: 'Email already registered' });
        }
        const hashedPassword = await bcrypt.hash(password, 10); 
        const newUser = new User({
            first_name: firstName,
            last_name: lastName,
            email,
            password: hashedPassword,
            role: role_id,  
            createdBy: req.user ? req.user._id : null
        });
        await newUser.save();
        res.status(201).json({ message: 'User registered successfully' });
    } catch (error) {
        res.status(500).json({ message: 'Server error', error });
    }
};
export const loginUser = async (req, res) => {
    const { email, password } = req.body;
    try {
        const user = await findUserByEmail(email);
        if (!user) {
            return res.status(404).json({ message: 'User not found' });
        }
        const isMatch = await bcrypt.compare(password, user.password);
        if (!isMatch) {
            return res.status(400).json({ message: 'Invalid credentials' });
        }
        const token = jwt.sign({ id: user._id, role: user.role }, JWT_SECRET, {
            expiresIn: JWT_EXPIRES_IN,
        });

        res.status(200).json({ token, role: user.role });
    } catch (error) {
        res.status(500).json({ message: 'Server error', error });
    }
};
