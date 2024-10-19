import jwt from "jsonwebtoken";
import { UserModel } from "../models/userSchema.js";
import { AdminModel } from "../models/adminSchema.js";

export const authenticateToken = async (req, res, next) => {
    const authHeader = req.headers.authorization;
    const token = authHeader && authHeader.split(" ")[1];

    if (!token) {
        return res.status(401).json({ message: "Authorization token missing" });
    }

    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET_KEY);

        if (!decoded.role) {
            return res.status(400).json({ message: "Token is missing role information" });
        }

        let user;

        // Log the decoded token for debugging
        console.log("Decoded Token:", decoded);

        if (decoded.role === "User") {
            user = await UserModel.findById(decoded.id);
        } else if (decoded.role === "Admin") {
            user = await AdminModel.findById(decoded.id);
        } else {
            return res.status(400).json({ message: "Invalid role in token" });
        }

        if (!user) {
            return res.status(404).json({ message: `${decoded.role} not found with ID: ${decoded.id}` });
        }

        req.user = user; 
        next();
    } catch (error) {
        // Log specific error for debugging
        console.error("Token verification error:", error);

        // Handle specific JWT errors
        if (error.name === "JsonWebTokenError") {
            return res.status(403).json({ message: "Invalid token", error: error.message });
        } else if (error.name === "TokenExpiredError") {
            return res.status(403).json({ message: "Token has expired", error: error.message });
        }

        // General error message for unexpected errors
        return res.status(500).json({ message: "An error occurred during token verification", error: error.message });
    }
};
