import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Bar } from 'react-chartjs-2';

const Dashboard = () => {
  const [data, setData] = useState({});
  const [chartData, setChartData] = useState({});

  useEffect(() => {
    axios.post('/analyze-sensor-data', { sensor_data: {}, maintenance_logs: {} })
      .then(response => {
        setData(response.data);
        setChartData({
          labels: ['Jan', 'Feb', 'Mar', 'Apr'],
          datasets: [{
            label: 'Sensor Data',
            data: [12, 19, 3, 5],
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
          }]
        });
      })
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>Dashboard</h1>
      <Bar data={chartData} />
    </div>
  );
};

export default Dashboard;


