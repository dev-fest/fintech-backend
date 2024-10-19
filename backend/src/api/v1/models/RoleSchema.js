import mongoose from "mongoose";


const roleSchema = new mongoose.Schema({
  role_id: {
    type: Number,
    required: true,
    min: [1, "Role ID must be a positive integer."],
    unique: true,  
  },
  role_name: {
    type: String,
    required: true,
    minlength: [3, "Role name must contain at least 3 characters."],
    maxlength: [50, "Role name must contain at most 50 characters."],
    validate: {
      validator: function (v) {
        return /^[A-Za-z]+$/.test(v); 
      },
      message: "Role name must contain only letters.",
    },
  },
});


const Role = mongoose.model("Role", roleSchema);

export default Role;
