import React, { useEffect, useState } from 'react';
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || '';

const ChatHistory = ({ selectChat, deleteChat }) => {
  const [chats, setChats] = useState([]);

  useEffect(() => {
    fetchChatHistory();
  }, []);

  const fetchChatHistory = async () => {
    try {
      const response = await axios.get(`${API_URL}/api/chats`);
      setChats(response.data);
    } catch (error) {
      console.error('Error fetching chat history:', error);
    }
  };

  const handleDeleteChat = async (chatId) => {
    try {
      await axios.delete(`${API_URL}/api/chats/${chatId}`);
      fetchChatHistory(); // Refresh chat history after deletion
    } catch (error) {
      console.error('Error deleting chat:', error);
    }
  };

  return (
    <div className="chat-history">
      <h2>Chat History</h2>
      <ul>
        {chats.map(chat => (
          <li key={chat.id}>
            <button onClick={() => selectChat(chat.id)}>Chat {chat.id}</button>
            <button onClick={() => handleDeleteChat(chat.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ChatHistory;


