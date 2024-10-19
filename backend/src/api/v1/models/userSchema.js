import mongoose from "mongoose";

const userSchema = new mongoose.Schema({
  user_id: {
    type: Number,
    unique: true,
    min: [1, "User ID must be a positive integer."],
  },
  first_name: {
    type: String,
    required: true,
    minlength: [2, "First name must contain at least 2 characters."],
    maxlength: [30, "First name must contain at most 30 characters."],
    validate: {
      validator: function (v) {
        return /^[A-Za-z]+$/.test(v); 
      },
      message: "First name must contain only letters.",
    },
  },
  last_name: {
    type: String,
    required: true,
    minlength: [2, "Last name must contain at least 2 characters."],
    maxlength: [30, "Last name must contain at most 30 characters."],
    validate: {
      validator: function (v) {
        return /^[A-Za-z]+$/.test(v); 
      },
      message: "Last name must contain only letters.",
    },
  },
  email: {
    type: String,
    required: true,
    unique: true,
    match: [/.+@.+\..+/, "Please enter a valid email address."],
  },
  password: {
    type: String,
    required: true,
    minlength: [8, "Password must contain at least 8 characters."],
  },
  role: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "Role",
    required: true,
  },
});


const User = mongoose.model("User", userSchema);

export default User;
