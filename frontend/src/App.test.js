import { act, render, screen } from '@testing-library/react';
import App from './App';
import { BrowserRouter } from 'react-router-dom';
import axios from 'axios';

afterEach(() => jest.restoreAllMocks());

test('renders the welcome page', async () => {
  jest.spyOn(axios, 'get').mockResolvedValue({
    data: { status: 'success', data: [] },
  });
  await act(async () => {
    render(<App />, { wrapper: BrowserRouter });
  });
  expect(await screen.findByText(/Welcome/i)).toBeInTheDocument();
});
