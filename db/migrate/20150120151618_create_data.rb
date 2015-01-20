class CreateData < ActiveRecord::Migration
  def change
    create_table :data do |t|
      t.text     :title
      t.text     :content
      t.string   :class_name

      t.timestamps null: false
    end
  end
end
