import { render, screen } from '@testing-library/react';
import App from './App';

test('renders the Virtual Try-On heading', () => {
  render(<App />);
  expect(screen.getByText(/virtual try-on/i)).toBeInTheDocument();
});
