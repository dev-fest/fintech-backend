import express from 'express';
import authRoutes from './authRoutes.js';
import router from './adminRoutes.js';

const routes = express.Router();

routes.use('/auth', authRoutes);
// routes.use('/users', userRoutes);
routes.use('/admin', router);

export default routes;
