import React, { useState, useEffect, useRef } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState('');
  const [chat, setChat] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  // Add welcome message when component mounts
  useEffect(() => {
    setChat([{ type: 'bot', text: "Hi! I'm Aditi's AI Chatbot. How can I help you today? 😊" }]);
  }, []);

  const sendMessage = async () => {
    if (!message.trim()) return;

    const userMsg = { type: 'user', text: message };
    setChat((prev) => [...prev, userMsg]);
    setMessage('');
    setIsLoading(true);

    try {
      const response = await fetch('https://chatbot-qxgm.onrender.com/chat/api', {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message.trim() }),
      });

      if (!response.ok) {
        throw new Error(`Server responded with status: ${response.status}`);
      }

      const data = await response.json();
      const botMsg = { type: 'bot', text: data.reply };
      setChat((prev) => [...prev, botMsg]);
      
    } catch (err) {
      console.error('Chat error:', err);
      const botMsg = { 
        type: 'bot', 
        text: 'Sorry, I cannot connect to the chatbot service right now. Please try again later.' 
      };
      setChat((prev) => [...prev, botMsg]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !isLoading) {
      sendMessage();
    }
  };

  const clearChat = () => {
    setChat([{ type: 'bot', text: "Hi! I'm Aditi's AI Chatbot. How can I help you today? 😊" }]);
  };

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [chat]);

  return (
    <div className="chat-container">
      <div className="chat-header">
        <h1>🤖 Aditi's AI Chatbot</h1>
        <button className="clear-btn" onClick={clearChat}>Clear Chat</button>
      </div>
      
      <div className="chat-box">
        {chat.map((msg, i) => (
          <div key={i} className={`message ${msg.type}`}>
            {msg.text}
          </div>
        ))}
        {isLoading && (
          <div className="message bot">
            <div className="typing-indicator">
              <span className="dot"></span>
              <span className="dot"></span>
              <span className="dot"></span>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>
      
      <div className="input-area">
        <input
          type="text"
          value={message}
          placeholder="Type your message here..."
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={handleKeyPress}
          disabled={isLoading}
        />
        <button 
          onClick={sendMessage} 
          disabled={isLoading || !message.trim()}
          className="send-btn"
        >
          {isLoading ? '⏳' : '📤'}
        </button>
      </div>
    </div>
  );
}

export default App;