import { useState, useEffect } from "react";

function App() {
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");
  const [location, setLocation] = useState("");
  const [disasterType, setDisasterType] = useState("");
  const [description, setDescription] = useState("");

  const [sosList, setSosList] = useState([]);

  const [stats, setStats] = useState({
    total_requests: 0,
    high_priority: 0,
    active_teams: 0,
  });

  const loadSOS = async () => {
    const response = await fetch("http://127.0.0.1:5000/sos");
    const data = await response.json();
    setSosList(data);
  };

  const loadDashboard = async () => {
    const response = await fetch("http://127.0.0.1:5000/dashboard");
    const data = await response.json();
    setStats(data);
  };

  useEffect(() => {
    loadSOS();
    loadDashboard();
  }, []);

  const submitSOS = async () => {
    const response = await fetch("http://127.0.0.1:5000/sos", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name,
        phone,
        location,
        disaster_type: disasterType,
        description,
      }),
    });

    const data = await response.json();

    alert(data.message);

    setName("");
    setPhone("");
    setLocation("");
    setDisasterType("");
    setDescription("");

    loadSOS();
    loadDashboard();
  };

  return (
    <div className="container mt-4">

      <div className="bg-danger text-white text-center p-4 rounded mb-4">
        <h1>🚨 DisasterOps AI</h1>
        <h4>AI Powered Emergency Response System</h4>
      </div>

      <div className="row mb-4">
        <div className="col-md-4">
          <div className="card text-center border-primary">
            <div className="card-body">
              <h5>Total SOS Requests</h5>
              <h2>{stats.total_requests}</h2>
            </div>
          </div>
        </div>

        <div className="col-md-4">
          <div className="card text-center border-danger">
            <div className="card-body">
              <h5>High Priority Cases</h5>
              <h2>{stats.high_priority}</h2>
            </div>
          </div>
        </div>

        <div className="col-md-4">
          <div className="card text-center border-success">
            <div className="card-body">
              <h5>Active Rescue Teams</h5>
              <h2>{stats.active_teams}</h2>
            </div>
          </div>
        </div>
      </div>

      <div className="card mb-4">
        <div className="card-header bg-dark text-white">
          Create SOS Request
        </div>

        <div className="card-body">

          <input
            className="form-control mb-3"
            placeholder="Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />

          <input
            className="form-control mb-3"
            placeholder="Phone Number"
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
          />

          <input
            className="form-control mb-3"
            placeholder="Location"
            value={location}
            onChange={(e) => setLocation(e.target.value)}
          />

          <input
            className="form-control mb-3"
            placeholder="Disaster Type"
            value={disasterType}
            onChange={(e) => setDisasterType(e.target.value)}
          />

          <textarea
            className="form-control mb-3"
            rows="4"
            placeholder="Describe the emergency"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />

          <button
            className="btn btn-danger w-100"
            onClick={submitSOS}
          >
            Submit SOS
          </button>

        </div>
      </div>

      <div className="card">
        <div className="card-header bg-primary text-white">
          SOS Requests
        </div>

        <div className="card-body">

          <table className="table table-striped table-bordered">

            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Location</th>
                <th>Disaster</th>
                <th>Priority</th>
                <th>Assigned Team</th>
                <th>Status</th>
              </tr>
            </thead>

            <tbody>
              {sosList.map((sos) => (
                <tr key={sos.id}>
                  <td>{sos.id}</td>
                  <td>{sos.name}</td>
                  <td>{sos.location}</td>
                  <td>{sos.disaster_type}</td>

                  <td>
                    {sos.priority >= 5 ? (
                      <span className="badge bg-danger">
                        High ({sos.priority})
                      </span>
                    ) : sos.priority >= 3 ? (
                      <span className="badge bg-warning text-dark">
                        Medium ({sos.priority})
                      </span>
                    ) : (
                      <span className="badge bg-success">
                        Low ({sos.priority})
                      </span>
                    )}
                  </td>

                  <td>{sos.assigned_team}</td>
                  <td>{sos.status}</td>
                </tr>
              ))}
            </tbody>

          </table>

        </div>
      </div>

    </div>
  );
}

export default App;