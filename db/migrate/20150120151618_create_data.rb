class CreateData < ActiveRecord::Migration
  def change
    create_table :data do |t|
      t.text     :title
      t.text     :content,      null: false
      t.string   :class_name,   null: false
      t.string   :file_name,    null: false
      t.integer  :index_order,  null: false

      t.timestamps null: false
    end

    add_index :data, :class_name
  end
end
