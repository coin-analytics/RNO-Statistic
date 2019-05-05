def build_models(db):
    class _KickLog(db.Model):
        __table_name__ = "kick_log"

        id = db.Column(db.Integer, primary_key=True)
        wallet = db.Column(db.String(128), nullable=False)
        weight = db.Column(db.Float, nullable=False)
        archi = db.Column(db.String(50), nullable=True)
        hertz = db.Column(db.Float, nullable=True)
        threads = db.Column(db.Integer, nullable=False)

        def __init__(self, wallet, weight, archi, hertz, threads):
            self.wallet = wallet
            self.weight = weight
            self.archi = archi      or None
            self.hertz = hertz      or None
            self.threads = threads   or None

        def __repr__(self):
            return f"<KickLog('{self.wallet}', '{self.weight}' with '{self.archi}', {self.hertz} x {self.thread})>"

    class _MinedCoin(db.Model):
        __table_name = "mining_log"

        id = db.Column(db.Integer, primary_key=True)
        wallet = db.Column(db.String(128), nullable=False)
        weight = db.Column(db.Float, nullable=False)
        cores = db.Column(db.Integer, nullable=True)
        solve_time = db.Column(db.Integer, nullable=True)
        coin = db.Column(db.Float, nullable=False)
        hashString = db.Column(db.String(12), nullable=False)
        nonce = db.Column(db.Integer, nullable=False)
        nbit = db.Column(db.Integer, nullable=False)

    class Models:
        KickLog=_KickLog
        MinedCoin=_MinedCoin

    return Models

