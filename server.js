require('dotenv').config();
const express = require('express');
const cors = require('cors');
const nodemailer = require('nodemailer');
const twilio = require('twilio');

const app = express();
app.use(cors());
app.use(express.json());

// Set up Nodemailer transporter
const transporter = nodemailer.createTransport({
  service: 'gmail', // or other service
  auth: {
    user: process.env.EMAIL_USER,
    pass: process.env.EMAIL_APP_PASSWORD
  }
});

// Set up Twilio client
let twilioClient;
if (process.env.TWILIO_ACCOUNT_SID && process.env.TWILIO_AUTH_TOKEN) {
  twilioClient = twilio(process.env.TWILIO_ACCOUNT_SID, process.env.TWILIO_AUTH_TOKEN);
}

app.post('/api/alert/email', async (req, res) => {
  const { to, subject, text } = req.body;
  
  if (!process.env.EMAIL_USER || !process.env.EMAIL_APP_PASSWORD) {
    return res.status(500).json({ error: 'Email service is not configured on the server. Please add credentials to .env.' });
  }

  try {
    await transporter.sendMail({
      from: `"HeatShield AI Alert" <${process.env.EMAIL_USER}>`,
      to,
      subject,
      text
    });
    res.json({ success: true, message: 'Email sent successfully.' });
  } catch (error) {
    console.error('Email error:', error);
    res.status(500).json({ error: error.message || 'Failed to send email.' });
  }
});

app.post('/api/alert/sms', async (req, res) => {
  const { to, body } = req.body;

  if (!twilioClient || !process.env.TWILIO_PHONE_NUMBER) {
    return res.status(500).json({ error: 'Twilio SMS service is not configured on the server. Please add credentials to .env.' });
  }

  try {
    await twilioClient.messages.create({
      body,
      from: process.env.TWILIO_PHONE_NUMBER,
      to
    });
    res.json({ success: true, message: 'SMS sent successfully.' });
  } catch (error) {
    console.error('SMS error:', error);
    res.status(500).json({ error: error.message || 'Failed to send SMS.' });
  }
});

// Export the Express API for Vercel Serverless
module.exports = app;

if (process.env.NODE_ENV !== 'production') {
  const PORT = process.env.PORT || 3000;
  app.listen(PORT, () => {
    console.log(`HeatShield Alert backend running on http://localhost:${PORT}`);
  });
}
