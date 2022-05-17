import React, { useState } from 'react';
import Form from './components/Form';
import FiltersAndOrderings from './components/FiltersAndOrderings';
import SpendingList from './components/SpendingList';
import Layout from './components/Layout';

export default function App() {
  const [spendings, setSpendings] = useState([]);

  return (
    <>
      <Layout>
        <Form
          spendings={spendings}
          setSpendings={setSpendings}
        />
        <FiltersAndOrderings
          setSpendings={setSpendings}
        />
        <SpendingList
          spendings={spendings}
          setSpendings={setSpendings}
        />
      </Layout>
    </>
  );
}
