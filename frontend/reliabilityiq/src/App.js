import React, { useState } from 'react';
import Dashboard from './components/Dashboard';
import Upload from './components/Upload';
import ChatHistory from './components/ChatHistory';

const App = () => {
  const [selectedChat, setSelectedChat] = useState(null);

  const handleSelectChat = (chatId) => {
    setSelectedChat(chatId);
  };

  const handleDeleteChat = (chatId) => {
    // Logic to delete chat
  };

  return (
    <div className="App">
      <h1>ReliabilityIQ</h1>
      <div className="main-content">
        <ChatHistory selectChat={handleSelectChat} deleteChat={handleDeleteChat} />
        <div className="chat-window">
          {/* Render chat window based on selectedChat */}
          {selectedChat ? (
            <div>Chat {selectedChat} is selected</div>
          ) : (
            <div>Select a chat from the history</div>
          )}
        </div>
      </div>
      <Dashboard />
      <Upload />
    </div>
  );
};

export default App;



