import mongoose from 'mongoose';

const adminSchema = new mongoose.Schema({
    firstName: { 
        type: String,
        required: true,
        trim: true
    },
    lastName: {
        type: String,
        required: true,
        trim: true
    },
    email: {
        type: String,
        required: true,
        unique: true,
        trim: true,
        validate: {
            validator: function(v) {
                return /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/.test(v);
            },
            message: 'Invalid email format'
        }
    },
    password: {
        type: String,
        required: true,
        minlength: 6
    },
    role: {
        type: String,
        enum: ["Admin"],
        default: "Admin",
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
    companyName: { 
        type: String,
        required: true, 
        trim: true
    },
    field: { 
        type: String,
        required: true, 
        trim: true
    }
}, { timestamps: true });

const AdminModel = mongoose.model('Admin', adminSchema);
export { AdminModel };
