# SpotPapers

SpotPapers is a Python application that retrieves wallpapers from the Windows Spotlight feature and saves them to a specified folder.

## Features

- Fetches wallpapers from the Windows Spotlight location.
- Saves wallpapers to a user-defined folder.

## Installing & Setup

- Install spotpapers

    ```bash
    pip install spotpapers
    ```

- Pass the API for AI Renaming (air) with the flag `--air` or setting the environment varable `GROQ_API_KEY`

## Working

1. Running the application

    ```bash
    spotpapers
    ```

    >[!TIP]  
    > Try using the `--help` flag to get more info.

2. The wallpapers will be fetched from the following location:

    ```text
    C:\Users\user\AppData\Local\Packages\Microsoft.Windows ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets
    ```

3. The wallpapers will be saved to the `Pictures\Spotlight Wallpapers` folder.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

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

## License

This project is licensed under the MIT License.

## Contact

For any questions or suggestions, please contact `advaith@glitchy.systems`.
