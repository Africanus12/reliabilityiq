import React from 'react';
import Dashboard from './components/Dashboard';
import Upload from './components/Upload';

const App = () => {
  return (
    <div className="App">
      <h1>ReliabilityIQ</h1>
      <Dashboard />
      <Upload />
    </div>
  );
};

export default App;
