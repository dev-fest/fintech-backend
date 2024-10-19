import jwt from 'jsonwebtoken';

const generateToken = (user) => {
  const payload = {
    id: user._id,
    role: user.role,
    fullName: user.fullName,
    lastName: user.lastName,
    email: user.email,
  };

  const token = jwt.sign(payload, process.env.JWT_SECRET_KEY, {
    expiresIn: '24h', 
  });

  return token;
};

export default generateToken;
