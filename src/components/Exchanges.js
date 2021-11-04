import React from 'react';
import { Row, Col } from 'reactstrap';
import "./Exchanges.css"

export const Exchanges = ({ exchanges, recs}) => {
    return (
        <div>
            {exchanges.map(exchange => {
                let BuyBtn;
                let SellBtn;
                if (exchange.name === recs.buy) {
                    BuyBtn = <button className="xc-btn buy-btn buy-recommend">{exchange.ask}</button>;
                } else {
                    BuyBtn = <button className="xc-btn buy-btn">{exchange.ask}</button>; 
                }
                if (exchange.name === recs.sell) {
                    SellBtn = <button className="xc-btn sell-btn sell-recommend">{exchange.bid}</button>;
                } else {
                    SellBtn = <button className="xc-btn sell-btn">{exchange.bid}</button>; 
                } 
                return (
                    <Row key={exchange.name} className="exchange">
                        <Col className="logo">
                        <img src={ process.env.PUBLIC_URL + exchange.name + '.png' } alt={exchange.name} />
                        </Col>
                        <Col className="btn-col">
                            {BuyBtn}
                        </Col>
                        <Col className="btn-col">
                            {SellBtn}
                        </Col>
                    </Row>
                );
            })}
        </div>
    );
};