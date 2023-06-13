import * as React from 'react';
import styles from './Header.module.css';

const Header = () => {
    return (
        <header>
            <h1 className={styles.header}>Menu</h1>
        </header>
    )
}

export { Header }