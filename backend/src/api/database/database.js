import mongoose from 'mongoose';
import dotenv from 'dotenv';

dotenv.config(); 

mongoose.set("strictQuery", false);
const mongoDBURL = process.env.mongoDbURL; 

if (!mongoDBURL) {
  throw new Error("MongoDB connection URL is not defined in environment variables.");
}

async function main() {
  try {
    await mongoose.connect(mongoDBURL, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log("MongoDB connection established successfully!");
  } catch (err) {
    console.error("Error connecting to MongoDB:", err);
  }
}

main().catch((err) => console.log(err));
