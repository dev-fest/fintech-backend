import { findUserByEmail } from "./authController.js"; // Ensure .js is included
import bcrypt from 'bcrypt'; // Make sure bcrypt is imported if used in this file

export const sendResetPasswordCode = async (req, res) => {
    const { email, role } = req.body;

    try {
        const user = await findUserByEmail(email, role);
        if (!user) {
            return res.status(404).json({ message: `${role} not found` });
        }

        // Generate a reset code and expiry time
        const resetPasswordCode = Math.floor(100000 + Math.random() * 900000).toString(); // 6-digit code
        const resetPasswordExpires = Date.now() + 3600000; // 1 hour

        // Update user's reset code and expiry time
        user.resetPasswordCode = resetPasswordCode;
        user.resetPasswordExpires = resetPasswordExpires;
        await user.save();

        // You can send an email with the reset code to the user here
        res.status(200).json({ message: 'Reset code sent to email' });
    } catch (error) {
        res.status(500).json({ message: 'Server error', error });
    }
};

// Reset Password (common for both Admin and User)
export const resetPassword = async (req, res) => {
    const { email, resetPasswordCode, newPassword, role } = req.body;

    try {
        const user = await findUserByEmail(email, role);
        if (!user || user.resetPasswordCode !== resetPasswordCode || user.resetPasswordExpires < Date.now()) {
            return res.status(400).json({ message: 'Invalid or expired reset code' });
        }

        // Hash the new password
        const hashedPassword = await bcrypt.hash(newPassword, 10);

        // Update the user's password and clear reset code and expiry time
        user.password = hashedPassword;
        user.resetPasswordCode = undefined;
        user.resetPasswordExpires = undefined;
        await user.save();

        res.status(200).json({ message: 'Password reset successfully' });
    } catch (error) {
        res.status(500).json({ message: 'Server error', error });
    }
};
