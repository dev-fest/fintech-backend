import { AdminModel } from '../models/adminSchema.js';
import { hashPassword } from '../../helper/passwordHelper.js';

const adminController = {
    getAdmins: async (req, res) => {
        try {
            if (req.params.id) {
                const admin = await AdminModel.findById(req.params.id);
                if (!admin) {
                    return res.status(404).json({ message: 'Admin not found' });
                }
                return res.status(200).json(admin);
            } else {
                const admins = await AdminModel.find();
                return res.status(200).json(admins);
            }
        } catch (error) {
            return res.status(500).json({ message: 'Server error', error });
        }
    },
    updateAdmin: async (req, res) => {
        try {
            const { fullName, lastName, email, password } = req.body;

            let hashedPassword;
            if (password) {
                hashedPassword = await hashPassword(password); 
            }
            const updatedAdmin = await AdminModel.findByIdAndUpdate(
                req.params.id,
                {
                    ...(fullName && { fullName }),
                    ...(lastName && { lastName }),
                    ...(email && { email }),
                    ...(hashedPassword && { password: hashedPassword }),
                },
                { new: true }
            );

            if (!updatedAdmin) {
                return res.status(404).json({ message: 'Admin not found' });
            }

            res.status(200).json(updatedAdmin);
        } catch (error) {
            res.status(500).json({ message: 'Server error', error });
        }
    },
    deleteAdmin: async (req, res) => {
        try {
            const deletedAdmin = await AdminModel.findByIdAndDelete(req.params.id);
            if (!deletedAdmin) {
                return res.status(404).json({ message: 'Admin not found' });
            }
            res.status(200).json({ message: 'Admin deleted successfully' });
        } catch (error) {
            res.status(500).json({ message: 'Server error', error });
        }
    }
};

export default adminController;
