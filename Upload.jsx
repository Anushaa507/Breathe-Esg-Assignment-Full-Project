import { useState } from 'react'
import axios from 'axios'

export default function Upload() {
  const [file, setFile] = useState(null)

  const handleUpload = async () => {
    const formData = new FormData()

    formData.append('file', file)
    formData.append('company_id', 1)

    await axios.post(
      'http://localhost:8000/api/upload/sap/',
      formData
    )

    alert('Upload complete')
  }
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">
        Upload SAP CSV
      </h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button
        onClick={handleUpload}
        className="ml-4 border px-4 py-2"
      >
        Upload
      </button>
    </div>
  )
}