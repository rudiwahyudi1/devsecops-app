module.exports = {
  testEnvironment: 'node',

  transform: {
    '^.+\\.(js|jsx|ts|tsx)$': 'babel-jest',
  },

  moduleNameMapper: {
    '^react-native$': '<rootDir>/__mocks__/react-native.js',
  },

  setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],

  testMatch: ['**/__tests__/**/*.test.js'],
};
