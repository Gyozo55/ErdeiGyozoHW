import React, { useState } from 'react';
import Form from './components/Form';
import FiltersAndOrderings from './components/FiltersAndOrderings';
import SpendingList from './components/SpendingList';
import Layout from './components/Layout';

export default function App() {
  const [spendings, setSpendings] = useState([]);
  const [url, setUrl] = useState([`http://localhost:8000/api/get-all-spendings`]);

  return (
    <>
      <Layout>
        <Form
          spendings={spendings}
          setSpendings={setSpendings}
          setUrl={setUrl}
        />
        <FiltersAndOrderings
          setSpendings={setSpendings}
          url={url}
          setUrl={setUrl}
        />
        <SpendingList
          spendings={spendings}
          setSpendings={setSpendings}
          url={url}
        />
      </Layout>
    </>
  );
}
