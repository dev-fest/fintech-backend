import mongoose from 'mongoose';

const projectSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
        trim: true,
    },
    description: {
        type: String,
        required: false,
        trim: true,
    },
    startDate: {
        type: Date,
        required: true,
    },
    endDate: {
        type: Date,
        required: true,
    },
    budgetId: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Budget', 
        required: true,
    }
}, { timestamps: true });

const ProjectModel = mongoose.model('Project', projectSchema);
export { ProjectModel };
