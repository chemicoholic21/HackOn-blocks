# Travel Planner

<img title="Planner" align='right' src="/static/logo.svg" alt="Travel Planner Logo" width="150"/>

## Revolutionize Your Travel Experience with Blockchain

Welcome to the Travel Planner, an innovative blockchain-powered solution designed to transform how you plan and experience travel. By leveraging the power of blockchain technology, we ensure transparency, security, and decentralization in crafting seamless travel experiences. Whether you're planning a road trip, city excursion, or an international adventure, our platform simplifies the entire planning process by providing a personalized itinerary based on your preferences and budget.

<p align="center">
Make your travel dreams a reality. Start planning your next adventure with the Travel Itinerary Generator today!
</p>
<p align="center">
<i>Explore, discover, and make every trip unforgettable with the assurance of blockchain security.</i>
</p>

## Tokenization and Rewards: A Blockchain Innovation
To enhance user engagement and foster a community-driven platform, we have introduced a token system that incentivizes users to share their travel experiences, reviews, and itineraries. This system ensures that user contributions are recognized and rewarded transparently through smart contracts.

### How It Works:
- **Earning Tokens**: Users earn tokens for contributing valuable data such as:
  - Writing reviews of attractions and accommodations
  - Sharing personal itineraries
  - Providing tips and recommendations

Tokens are stored securely on the blockchain, ensuring that your contributions are immutable and rewarded fairly.

## Table of Contents

- [Travel Planner](#travel-planner)
  - [Tokenization and Rewards](#tokenization-and-rewards-a-blockchain-innovation)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Limitations & Future Work](#limitations--future-work)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Setup and Installation](#setup-and-installation)
  - [API Keys](#api-keys)
  - [Usage](#usage)
  - [License](#license)

## About

The Travel Planner is a cutting-edge platform that empowers travelers to effortlessly create personalized travel itineraries. By considering users' interests, budgets, and travel dates, this application generates comprehensive lists of activities, attractions, and accommodations. Leveraging blockchain technology, the platform ensures that all data and transactions are secure, transparent, and decentralized, providing an unparalleled level of trust and reliability.

## Limitations & Future Work
- Currently, the Planner works based on the user's source, destination, and time of travel.

**Future Work:**
- Enabling itinerary generation for multiple destinations.
- Integrating hotel and flight suggestions.
- **Real-time Collaboration:** Introducing real-time collaboration features, allowing users to share their itineraries with travel companions or collaborators securely through the blockchain.

## Features

- **Blockchain-Powered Security:** Ensures that all user data and transactions are secure, transparent, and tamper-proof.
- **Weather Forecast:** Provides a weather forecast for the destination during the entire travel period.
- **Travel Itinerary:** Generates a travel itinerary for the entire travel period within an optimal budget.

## Requirements

- Python 3.11
- Flask
- Flask-SQLAlchemy
- google-generativeai==0.2.2
- Solidity==0.8.0
- Truffle

## Setup and Installation

1. Clone the repository:
    ```shell
    git clone https://github.com/chemicoholic21/HackOn-blocks.git
    cd HackOn-blocks
    ```

2. Install the required packages:
    ```shell
    pip install -r requirements.txt
    ```

3. Compile the smart contracts using Truffle:
    ```shell
    truffle compile
    ```

4. Migrate the smart contracts to the blockchain:
    ```shell
    truffle migrate
    ```

## API Keys
- Visual Crossing Weather API Key: [Sign up](https://www.visualcrossing.com/weather-api) for a free account and get your API key.
- Google Palm API: [Sign up](https://makersuite.google.com) for a free account and get your API key.

## Usage
1. Create a `.env` file in the root directory and add your API keys:
    ```shell
    WEATHER_API_KEY='Your Visual Crossing Weather API Key'
    PALM_API_KEY='Your Google Palm API Key'
    ```

2. Run the application:
    ```shell
    python wsgi.py
    ```

## License

This project is licensed under the [Apache License 2.0](LICENSE) - see the [LICENSE](LICENSE) file for details.

