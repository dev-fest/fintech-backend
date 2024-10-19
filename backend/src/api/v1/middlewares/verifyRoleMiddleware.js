export const verifyRole = (...allowedRoles) => {
    return (req, res, next) => {
        if (!req.user) {
            return res.status(401).send("You are not authenticated");
        }
        if (allowedRoles.includes(req.user.role)) {
            return next();
        } else {
            return res.status(401).send("You are not allowed to access this resource");
        }
    };
};

