from ..db import db

journal_entry_movements = db.Table(
    'journal_entry_movements',
    db.Column(
        'journal_entry_id',
        db.ForeignKey('journal_entries.id'),
        primary_key=True),
    db.Column(
        'movement_id',
        db.ForeignKey('movements.id'),
        primary_key=True)
)

journal_entry_moods_before = db.Table(
    'journal_entry_moods_before',
    db.Column(
        'journal_entry_id',
        db.ForeignKey('journal_entries.id'),
        primary_key=True
    ),
    db.Column(
        'mood_before_id',
        db.ForeignKey('moods.id'),
        primary_key=True
    )
)

journal_entry_moods_after = db.Table(
    'journal_entry_moods_after',
    db.Column(
        'journal_entry_id',
        db.ForeignKey('journal_entries.id'),
        primary_key=True
    ),
    db.Column(
        'mood_after_id',
        db.ForeignKey('moods.id'),
        primary_key=True
    )
)