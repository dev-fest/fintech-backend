import express from "express";
import { authenticateToken } from "../middlewares/auth.js";
import adminController from "../controllers/adminController.js";
import { resetPassword, sendResetPasswordCode } from "../controllers/resetPasswordController.js";
import { verifyRole } from "../middlewares/verifyRoleMiddleware.js";
const router = express.Router();
router.get("/:id?", authenticateToken, verifyRole("Admin"), adminController.getAdmins);
router.patch("/:id", authenticateToken, adminController.updateAdmin);
router.delete("/:id", authenticateToken, adminController.deleteAdmin);
// router.post('/resetpassword', sendResetPasswordCode); 
// router.patch('/resetpassword/confirm/:adminId', resetPassword);

export default router;
