# SpotPapers

SpotPapers is a Python application that retrieves wallpapers from the Windows Spotlight feature and saves them to a specified folder.

## Features

- Fetches wallpapers from the Windows Spotlight location.
- Saves wallpapers to a user-defined folder.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Glitchyi/spotpapers
    ```

2. Navigate to the project directory:

    ```bash
    cd spotpapers
    ```

3. Create a virtual environment:

    ```bash
    python -m venv .env
    ```

4. Activate the virtual environment:

    ```bash
    source .env/Scripts/activate
    ```

5. Install the required dependencies:

    ```bash
    pip install -e .
    ```

## Usage

1. Activate the virtual environment:

    ```bash
    source .env/Scripts/activate
    ```

2. Run the application:

    ```bash
    spotpapers
    ```

3. The wallpapers will be fetched from the following location:

    ```text
    C:\Users\user\AppData\Local\Packages\Microsoft.Windows ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets
    ```

4. The wallpapers will be saved to the specified folder.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

For any questions or suggestions, please contact [your email].
