import mongoose from 'mongoose';

const roleSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
        trim: true,
    },
    permissions: {
        type: [String], 
        required: true,
    }
}, { timestamps: true });

const RoleModel = mongoose.model('Role', roleSchema);
export { RoleModel };
