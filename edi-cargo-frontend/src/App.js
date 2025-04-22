import React, { useState } from 'react';
import axios from 'axios';

// const BACKEND_URL = 'http://localhost:8000';
const BACKEND_URL = 'https://clearai-backend-container-app.lemonflower-9055be44.australiasoutheast.azurecontainerapps.io';

const defaultCargoItem = () => ({
  cargo_type: 'FCL',
  number_of_packages: 1,
  container_number: '',
  master_bill_number: '',
  house_bill_number: ''
});

export default function EDICargoGenerator() {
  const [cargoItems, setCargoItems] = useState([defaultCargoItem()]);
  const [ediOutput, setEdiOutput] = useState('');
  const [ediInput, setEdiInput] = useState('');
  // const [parsedItems, setParsedItems] = useState([]);

  const handleItemChange = (index, field, value) => {
    const updated = [...cargoItems];
    updated[index][field] = field === 'number_of_packages' ? parseInt(value) || '' : value.replace(/\n/g, '\n');
    console.log(updated)
    setCargoItems(updated);
  };

  const addCargoItem = () => {
    setCargoItems([...cargoItems, defaultCargoItem()]);
  };

  const generateEDI = async () => {
    try {
      console.log(cargoItems);
      console.log(BACKEND_URL + "/generate-edi");
      const response = await axios.post(BACKEND_URL + '/generate-edi', { cargo_items: cargoItems });
      console.log(response.data);
      setEdiOutput(response.data.edi_message);
    } catch (error) {
      alert('Error generating EDI ' + error);
    }
  };

  const parseEDI = async () => {
    try {
      console.log(ediInput);
      const response = await axios.post(BACKEND_URL + '/parse-edi', { edi_content: ediInput });
      console.log(response.data);
      // setParsedItems(response.data.cargo_items);
      setCargoItems(response.data.cargo_items);
    } catch (error) {
      alert('Error parsing EDI');
    }
  };

  return (
    <div className="container py-4 text-white min-vh-100">
      <h1 className="mb-4">EDI Cargo Report Generator</h1>

      <div className="row g-4" id="survey-form">
        {/* Cargo Items Panel */}
        <div className="col-lg-6">
          <div className="card custom-background text-white mb-3 rounded-xl">
            {cargoItems.map((item, index) => (
              <div className="card-body">
                <h5 className="card-title">Cargo Item #{index + 1}</h5>

                <div className="mb-3">
                  <label htmlFor="cargoType" className="form-label">
                    Cargo Type
                  </label>
                  <select
                    className="form-select"
                    id="cargoType"
                    value={item.cargo_type}
                    onChange={(e) => handleItemChange(index, 'cargo_type', e.target.value)}
                  >
                    <option value="FCL">FCL</option>
                    <option value="LCL">LCL</option>
                    <option value="LCL">FCX</option>
                  </select>
                </div>

                <div className="mb-3">
                  <label htmlFor="packages" className="form-label">
                    Number of Packages
                  </label>
                  <input
                    type="number"
                    className="form-control"
                    id="packages"
                    min="1"
                    value={item.number_of_packages}
                    onChange={(e) => handleItemChange(index, 'number_of_packages', e.target.value)}
                  />
                </div>

                <div className="mb-3">
                  <label htmlFor="containerNumber" className="form-label">
                    Container Number (Optional)
                  </label>
                  <input
                    type="text"
                    className="form-control"
                    value={item.container_number}
                    onChange={(e) => handleItemChange(index, 'container_number', e.target.value)}
                  />
                </div>

                <div className="mb-3">
                  <label htmlFor="masterBill" className="form-label">
                    Master Bill of Lading Number (Optional)
                  </label>
                  <input
                    type="text"
                    className="form-control"
                    value={item.master_bill_of_lading_number}
                    onChange={(e) => handleItemChange(index, 'master_bill_of_lading_number', e.target.value)}
                  />
                </div>

                <div className="mb-3">
                  <label htmlFor="houseBill" className="form-label">
                    House Bill of Lading Number (Optional)
                  </label>
                  <input
                    type="text"
                    className="form-control"
                    id="houseBill"
                    value={item.house_bill_of_lading_number}
                    onChange={(e) => handleItemChange(index, 'house_bill_of_lading_number', e.target.value)}
                  />
                </div>
              </div>
            ))}
            <div className="card-body">
              <div className="d-grid gap-2">
                <button onClick={addCargoItem} className="btn btn-outline-light">Add Cargo Item</button>
                <button onClick={generateEDI} className="btn btn-outline-light mb-2">
                  Generate EDI
                </button>
              </div>
            </div>
          </div>

          <div className="card custom-background text-white">
            <div className="card-body">
              <h5 className="card-title">Parse Existing EDI</h5>
              <textarea
                className="form-control mb-2"
                rows="4"
                placeholder="Paste existing EDI here to parse it into the form above"
                value={ediInput}
                onChange={(e) => setEdiInput(e.target.value)}
              ></textarea>
              <div className="d-grid">
                <button className="btn btn-outline-light" onClick={parseEDI} >
                  Parse EDI
                </button>
              </div>
            </div>
          </div>
        </div>

        {/* EDI Output */}
        <div className="col-lg-6">
          <div className="card custom-background text-white h-100">
            <div className="card-body">
              <h5 className="card-title">EDI Output</h5>
              <textarea
                className="form-control text-info"
                value={ediOutput}
                readOnly
                rows="8"
                style={{ backgroundColor: "#1e1e1e", fontFamily: "monospace", height: "90%" }}
              ></textarea>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
