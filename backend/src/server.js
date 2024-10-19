import express from 'express';
import dotenv from 'dotenv';
import cors from 'cors';
const app = express();
dotenv.config();
import routes from './api/v1/routes/index.js';
import "./api/database/database.js";
const PORT = process.env.PORT;
app.use(cors());
app.use(express.json());


app.use('/api/v1', routes);

app.listen(PORT, (error) => {
    if (!error) {
        console.log('Server is Successfully Running, and App is listening on port ' + PORT);
    } else {
        console.log('Error occurred, server can\'t start ', error);
    }
});
