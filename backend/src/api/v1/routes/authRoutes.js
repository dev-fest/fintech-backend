import express from "express";
import { loginUser, registerUserGeneral} from "../controllers/authController.js";
const authRoutes = express.Router();
authRoutes.post("/register", registerUserGeneral);
authRoutes.post("/login", loginUser);

export default authRoutes;
