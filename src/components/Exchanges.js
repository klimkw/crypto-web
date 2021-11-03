import React from 'react';
import { Button, Row, Col } from 'reactstrap';
import "./Exchanges.css"

export const Exchanges = ({ exchanges }) => {
    return (
        <div>
            {exchanges.map(exchange => {
                return (
                    <Row key={exchange.name} className="exchange">
                        <Col className="logo">
                        <img src={ process.env.PUBLIC_URL + exchange.name + '.png' } alt={exchange.name} />
                        </Col>
                        <Col>
                            <Button className="xcBtn btn-block btn-outline-success">
                                {exchange.ask}
                            </Button>
                        </Col>
                        <Col>
                            <Button className="xcBtn btn-block btn-outline-danger">
                                {exchange.bid}
                            </Button>
                        </Col>
                    </Row>
                );
            })}
        </div>
    );
};