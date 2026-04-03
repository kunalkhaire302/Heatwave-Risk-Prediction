require('dotenv').config();
const express = require('express');
const cors = require('cors');
const { Resend } = require('resend'); // Replaced Nodemailer due to Render SMTP blocking

const app = express();
const path = require('path');

app.use(cors());
app.use(express.json());

// Serve static files from the current directory
app.use(express.static(__dirname));

// Serve the frontend interface on the root URL
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'heatwave_predictor.html'));
});

// Set up Resend client
const resend = process.env.RESEND_API_KEY ? new Resend(process.env.RESEND_API_KEY) : null;


app.post('/api/alert/email', async (req, res) => {
  const { to, subject, text } = req.body;
  
  if (!process.env.RESEND_API_KEY) {
    return res.status(500).json({ error: 'Email service is not configured on the server. Please add RESEND_API_KEY credentials.' });
  }

  try {
    const response = await resend.emails.send({
      from: 'HeatShield AI Alert <onboarding@resend.dev>', // Free tier Resend requires onboarding domain
      to,
      subject,
      text
    });
    
    if (response.error) throw new Error(response.error.message);
    
    res.json({ success: true, message: 'Email sent successfully via Resend.' });
  } catch (error) {
    console.error('Email error:', error);
    res.status(500).json({ error: error.message || 'Failed to send email.' });
  }
});


// Export the Express API for Vercel Serverless
module.exports = app;

if (require.main === module) {
  const PORT = process.env.PORT || 3000;
  app.listen(PORT, () => {
    console.log(`HeatShield Alert backend running on http://localhost:${PORT}`);
  });
}
