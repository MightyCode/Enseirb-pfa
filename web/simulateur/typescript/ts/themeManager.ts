enum Theme {
    Light,
    Dark
};

export default class ThemeManager {

    _theme: Theme;
    _element: HTMLInputElement;

    constructor(_element: HTMLInputElement) {
        this._element = _element;

        // Read local storage to see if a theme is set
        const theme = localStorage.getItem('theme');

        // If a theme is set, set it
        if (theme) {
            this.theme = parseInt(theme);

            if (this._theme === Theme.Light) {
                // set checkbox to checked
                this._element.checked = true;
            }
        } else {
            // Defaults theme to Dark
            this.theme = Theme.Dark;
        }
    }


    /**
     * Sets the theme of the application
     */
    set theme(theme: Theme) {
        // Set the current theme
        this._theme = theme;
        
        // Call the appropriate method to update the CSS
        switch (theme) {
            case Theme.Dark:
                this.updateCSSDark();
                break;
            case Theme.Light:
                this.updateCSSLight();
                break;
        }

        // Save the theme to local storage
        localStorage.setItem('theme', theme.toString());
    }

    /**
     * Switches theme to Light
    */
    updateCSSLight(): void {
        const body = document.body;

        // Set the CSS variables
        body.style.setProperty('--primary-color', '#dfe6e9');
        body.style.setProperty('--secondary-color', '#b2bec3');
        body.style.setProperty('--tertiary-color', '#a8b3b7');
    }

    /**
     * Switches theme to Dark
    */
    updateCSSDark(): void {
        const body = document.body;

        // Set the CSS variables
        body.style.setProperty('--primary-color', '#1B1B1B');
        body.style.setProperty('--secondary-color', '#292929');
        body.style.setProperty('--tertiary-color', '#383838');
    }

    switchTheme(): void {
        // Switch the theme
        this.theme = this._theme === Theme.Dark ? Theme.Light : Theme.Dark;
    }

}