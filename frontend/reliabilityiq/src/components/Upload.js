import React, { useState } from 'react';
import axios from 'axios';

const Upload = () => {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = () => {
    const formData = new FormData();
    formData.append('file', file);

    axios.post('/interpret-report', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
    .then(response => console.log(response.data))
    .catch(error => console.error(error));
  };

  return (
    <div>
      <h1>Upload Maintenance Report</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
};

export default Upload;



