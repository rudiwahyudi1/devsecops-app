import { render, screen } from "@testing-library/react";
import App from "./App";

test("renders app text", () => {
  render(<App />);
  expect(screen.getByText(/react ci\/cd ready/i)).toBeInTheDocument();
});
