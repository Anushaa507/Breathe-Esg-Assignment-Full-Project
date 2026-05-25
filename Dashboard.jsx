import { useEffect, useState } from 'react'
import axios from 'axios'

export default function Dashboard() {
  const [records, setRecords] = useState([])

  useEffect(() => {
    fetchRecords()
  }, [])

  const fetchRecords = async () => {
    const response = await axios.get(
      'http://localhost:8000/api/emissions/'
    )

    setRecords(response.data)
  }
  const approveRecord = async (id) => {
    await axios.post(
      `http://localhost:8000/api/emissions/${id}/approve/`
    )

    fetchRecords()
  }

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-6">
        ESG Analyst Dashboard
      </h1>
      <table className="w-full border">
        <thead>
          <tr>
            <th>ID</th>
            <th>Scope</th>
            <th>Category</th>
            <th>Emissions</th>
            <th>Status</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {records.map(record => (
            <tr key={record.id}>
              <td>{record.id}</td>
              <td>{record.scope}</td>
              <td>{record.category}</td>
              <td>{record.emissions_kg_co2e}</td>
              <td>{record.approval_status}</td>

              <td>
                <button
                  onClick={() => approveRecord(record.id)}
                >
                  Approve
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}