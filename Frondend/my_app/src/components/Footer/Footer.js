import * as React from "react";
import styles from "./Footer.module.css"
import { BsFacebook, BsGithub, BsTelegram } from 'react-icons/bs';


const Footer = () => {
    return (
        <>
            <div className={styles.phantom}></div>
            <div className={styles.footer}>
                <a href="https://www.facebook.com/abror.doniyorov" target={"_blank"} rel="noreferrer" className={styles.social_links}>
                    <BsFacebook />
                </a>
                <a href="https://www.github.com/DoniyorovAbror" target={"_blank"} rel="noreferror" className={styles.social_links}>
                    <BsGithub />
                </a>
                <a href="https://t.me./abror_doniyorov_termiz" target={"_blank"} rel="noreferror" className={styles.social_links}>
                    <BsTelegram />
                </a>
                <p className="copyright"> &copy; 2023 </p>
            </div>
        </>
    )
}

export { Footer };