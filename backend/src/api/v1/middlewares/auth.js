import jwt from "jsonwebtoken";
import User from "../models/userSchema.js";
export const authenticateToken = async (req, res, next) => {
    const authHeader = req.headers.authorization;
    const token = authHeader && authHeader.split(" ")[1];
    if (!token) {
        return res.status(401).json({ message: "Authorization token missing" });
    }
    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET_KEY);
        if (!decoded.role || decoded.role !== "User") {
            return res.status(400).json({ message: "Invalid or missing role in token" });
        }
        const user = await User.findById(decoded.id);

        if (!user) {
            return res.status(404).json({ message: `User not found with ID: ${decoded.id}` });
        }  
        req.user = user; 
        next();
    } catch (error) {
        console.error("Token verification error:", error);
        if (error.name === "JsonWebTokenError") {
            return res.status(403).json({ message: "Invalid token", error: error.message });
        } else if (error.name === "TokenExpiredError") {
            return res.status(403).json({ message: "Token has expired", error: error.message });
        }
        return res.status(500).json({ message: "An error occurred during token verification", error: error.message });
    }
};
