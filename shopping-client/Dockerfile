# Use the official Node.js 16 image
FROM node:18

# Set the working directory
WORKDIR app/

# Copy the entire project to the working directory
COPY . /app

# Install dependencies
RUN npm install --force
RUN npm install react-scripts --save
# Build the React app
RUN npm run build

# Expose the port the app runs on
EXPOSE 3000

# Serve the React app with a static server
CMD ["npm", "start"]