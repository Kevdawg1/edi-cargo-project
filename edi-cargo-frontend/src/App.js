import React, { useState } from 'react';
import axios from 'axios';

const BACKEND_URL = 'http://localhost:8000';

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

  const handleItemChange = (index, field, value) => {
    const updated = [...cargoItems];
    updated[index][field] = field === 'number_of_packages' ? parseInt(value) || '' : value;
    setCargoItems(updated.replace(/\n/g, '\n'));
  };

  const addCargoItem = () => {
    setCargoItems([...cargoItems, defaultCargoItem()]);
  };

  const generateEDI = async () => {
    try {
      console.log(cargoItems);
      const response = await axios.post(BACKEND_URL+'/generate-edi', {cargo_items: cargoItems});
      console.log(response.data);
      setEdiOutput(response.data.edi_message);
    } catch (error) {
      alert('Error generating EDI ' + error);
    }
  };

  const parseEDI = async () => {
    try {
      console.log(ediInput);
      const response = await axios.post(BACKEND_URL+'/parse-edi', { edi_content: ediInput });
      console.log(response.data);
      setParsedItems(response.data.cargo_items);
      setCargoItems(response.data.cargo_items);
    } catch (error) {
      alert('Error parsing EDI');
    }
  };

  return (
    <div className="grid grid-cols-2 gap-4 p-6 text-white bg-black min-h-screen">
      <div>
        <h2 className="text-xl font-bold mb-4">Cargo Items</h2>
        {cargoItems.map((item, index) => (
          <div key={index} className="mb-6 border p-4 rounded-xl border-white/20">
            <h3 className="text-lg font-semibold mb-2">Cargo Item #{index + 1}</h3>
            <label className="block mb-2">
              Cargo Type:
              <select
                value={item.cargo_type}
                onChange={(e) => handleItemChange(index, 'cargo_type', e.target.value)}
                className="w-full bg-gray-900 text-white p-2 rounded"
              >
                <option value="FCL">FCL</option>
                <option value="LCL">LCL</option>
                <option value="FCX">FCX</option>
              </select>
            </label>
            <label className="block mb-2">
              Number of Packages:
              <input
                type="number"
                min="1"
                value={item.number_of_packages}
                onChange={(e) => handleItemChange(index, 'number_of_packages', e.target.value)}
                className="w-full bg-gray-900 text-white p-2 rounded"
              />
            </label>
            <label className="block mb-2">
              Container Number (Optional):
              <input
                type="text"
                value={item.container_number}
                onChange={(e) => handleItemChange(index, 'container_number', e.target.value)}
                className="w-full bg-gray-900 text-white p-2 rounded"
              />
            </label>
            <label className="block mb-2">
              Master Bill of Lading Number (Optional):
              <input
                type="text"
                value={item.master_bill_number}
                onChange={(e) => handleItemChange(index, 'master_bill_of_lading_number', e.target.value)}
                className="w-full bg-gray-900 text-white p-2 rounded"
              />
            </label>
            <label className="block mb-2">
              House Bill of Lading Number (Optional):
              <input
                type="text"
                value={item.house_bill_number}
                onChange={(e) => handleItemChange(index, 'house_bill_of_lading_number', e.target.value)}
                className="w-full bg-gray-900 text-white p-2 rounded"
              />
            </label>
          </div>
        ))}
        <button onClick={addCargoItem} className="bg-blue-600 px-4 py-2 rounded mr-2">Add Cargo Item</button>
        <button onClick={generateEDI} className="bg-green-600 px-4 py-2 rounded">Generate EDI</button>
      </div>
      <div>
        <h2 className="text-xl font-bold mb-4">EDI Output</h2>
        <textarea
          value={ediOutput}
          readOnly
          className="w-full h-64 bg-gray-900 text-white p-2 rounded mb-4"
        />

        <h2 className="text-xl font-bold mb-2">Parse Existing EDI</h2>
        <textarea
          placeholder="Paste existing EDI here..."
          value={ediInput}
          onChange={(e) => setEdiInput(e.target.value)}
          className="w-full h-40 bg-gray-900 text-white p-2 rounded mb-2"
        />
        <button onClick={parseEDI} className="bg-yellow-600 px-4 py-2 rounded">Parse EDI</button>
      </div>
    </div>
  );
}
