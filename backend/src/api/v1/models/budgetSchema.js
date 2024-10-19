import mongoose from 'mongoose';

const budgetSchema = new mongoose.Schema({
    projectId: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Project',
        required: true,
    },
    amount: {
        type: Number,
        required: true,
    },
    currency: {
        type: String,
        required: true,
        trim: true,
        maxlength: 3, // ISO currency code format (USD, EUR)
    },
    year: {
        type: Number,
        required: true,
    }
}, { timestamps: true });

const BudgetModel = mongoose.model('Budget', budgetSchema);
export { BudgetModel };
