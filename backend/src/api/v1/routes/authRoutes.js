import express from "express";
import { registerAdmin, registerUserGeneral, loginUser } from "../controllers/authController.js";
import { authenticateToken } from "../middlewares/auth.js";
import { verifyRole } from "../middlewares/verifyRoleMiddleware.js";
const authRoutes = express.Router();
authRoutes.post("/register/admin", registerAdmin);
authRoutes.post("/register/user", authenticateToken, verifyRole("Admin"), registerUserGeneral);
authRoutes.post("/login", loginUser);

export default authRoutes;
