import mongoose from "mongoose";

const userSchema = new mongoose.Schema({
    fullName: {
        type: String,
        trim: true,
        maxlength: 50,
        required: false,
    },
    lastName: {
        type: String,
        trim: true,
        maxlength: 50,
        required: false,
    },
    email: {
        type: String,
        trim: true,
        maxlength: 50,
        required: true,
        unique: true,
    },
    password: {
        type: String,
        trim: true,
        maxlength: 255,
        required: true,
    },
    role: {
        type: String,
        enum: ["User"],
        default: "User",
    },
    refreshToken: {
        type: String,
        required: false,
    },
    resetPasswordCode: {
        type: String,
        required: false,
    },
    resetPasswordExpires: {
        type: Date,
        required: false,
    },
    createdBy: { 
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Admin', 
        required: true
    }
}, { timestamps: true });

const UserModel = mongoose.model("User", userSchema);
export { UserModel };
