import mongoose from "mongoose";

mongoose.set("strictQuery", false);
const mongoDBURL = "mongodb+srv://greylanisteur123:CWihvdE3IHnEV3eK@cluster0.i4xu4.mongodb.net/Cluster1?retryWrites=true&w=majority&appName=Cluster1";

if (!mongoDBURL) {
  throw new Error(
    "MongoDB connection URL is not defined in environment variables."
  );
}

async function main() {
  try {
    await mongoose.connect(mongoDBURL);
    console.log("MongoDB connection established successfully!");
  } catch (err) {
    console.error("Error connecting to MongoDB:", err);
  }
}

main().catch((err) => console.log(err));
